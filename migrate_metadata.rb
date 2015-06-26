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

def migrate_all_cre_info()

    begin
      res = DB2Database.connection.exec_query('
      SELECT DRAFT_ENTRY_CODE, REPL_INFILL_CODES_ REPL_DRAFT_ENTRY
      FROM T_DRAFT_ENTRY',
      'Migrating metadata')

      CRE_codes = Array.new
      res.each do | row |
        puts row['DRAFT_ENTRY_CODE']
      end

    rescue => e
        raise e
    ensure
        DB2Database::ActiveRecord::Base.clear_active_connections!
    end

    return json.to_s

end
