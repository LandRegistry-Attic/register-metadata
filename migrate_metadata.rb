require 'active_support/core_ext'
require 'active_record'
require 'activerecord-jdbc-adapter'
require 'yaml'
require 'openssl'
require 'base64'
require_relative 'db2lr-adaptor.rb'
require_relative 'db2lr-column.rb'
require_relative 'db2jcc4.jar'
require_relative 'db2jcc_javax.jar'
require_relative 'db2jcc_license_cisuz.jar'

dbconfig = YAML.load( File.open(File.dirname(__FILE__) + '/config/database.yml') )
ENV['RACK_ENV'] ||= 'development'

class DB2Database < ActiveRecord::Base
end

#Default to stupid development key
begin
	lr_encryption_key = File.open(File.dirname(__FILE__) + '/../../../lr-encoded-key') { |f| Base64.decode64(f.gets) }
rescue
	lr_encryption_key = 'this is the development encryption key'
end
cipher = OpenSSL::Cipher::Cipher.new('aes-256-cbc')
cipher.decrypt
cipher.key = lr_encryption_key
cipher.iv = Base64.decode64(dbconfig[ENV['RACK_ENV']]["enc_iv"])
password = cipher.update(Base64.decode64(dbconfig[ENV['RACK_ENV']]["enc_password"])) + cipher.final
dbconfig[ENV['RACK_ENV']][:password] = password

dbconfig[ENV['RACK_ENV']][:adapter_spec] = ::ArJdbc::DB2LR
DB2Database::ActiveRecord::Base.establish_connection(dbconfig[ENV['RACK_ENV']])
::ArJdbc::DB2LR.emulate_booleans = false

# Class to get columns for binds cheaply
class ColumnTypes
  # Get AR column object for given sql_type
  # @param sql_type [String] sql type
  # @return [Column] AR column
  def self.get_column(sql_type)
    DB2Database::ActiveRecord::Base.connection.jdbc_column_class.new('', nil, sql_type = sql_type)
  end
end

class RegisterMetadataDB < ActiveRecord::Base
end

RegisterMetadataDB.establish_connection(dbconfig["register_metadata_#{ENV['RACK_ENV']}"])

def migrate_all_cre_info()

    begin
      res = DB2Database.connection.exec_query("
      SELECT DRAFT_ENTRY_CODE, DRAFT_ENTRY_VERS, REPL_INFILL_CODES, REPL_DRAFT_ENTRY
      FROM T_DRAFT_ENTRY
			WHERE LANG_CODE = 'ENG'",
      'Migrating CRE')

      res.each_with_index do | row, i |

					sql = RegisterMetadataDB.send(:sanitize_sql_array, ["insert into public.cre (code, version, template, infills) VALUES(?,?,?,?)", row['draft_entry_code'], row['draft_entry_vers'], row['repl_draft_entry'], row['repl_infill_codes']])
					RegisterMetadataDB.connection.execute(sql)

      end

    rescue => e
        raise e
    ensure
        DB2Database::ActiveRecord::Base.clear_active_connections!
    end
end

migrate_all_cre_info()

def migrate_all_mdref_info()

	begin
		res = DB2Database.connection.exec_query("
		SELECT DRAFT_ENTRY_CODE, DRAFT_ENTRY_VERS, MD_REF, ENTRY_CODE_SEQ_NO
		FROM T_MD_DRAFT_ENTRY
		WHERE LANG_CODE = 'ENG'",
		'Migrating MDRef')

		res.each_with_index do | row, i |

				sql = RegisterMetadataDB.send(:sanitize_sql_array, ["insert into public.mdref (code, version, mdref, sequence) VALUES(?,?,?,?)", row['draft_entry_code'], row['draft_entry_vers'], row['md_ref'], row['entry_code_seq_no']])
				RegisterMetadataDB.connection.execute(sql)

		end

	rescue => e
			raise e
	ensure
			DB2Database::ActiveRecord::Base.clear_active_connections!
	end

end

migrate_all_mdref_info()
