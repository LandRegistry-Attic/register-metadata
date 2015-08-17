#!/usr/bin/env bash
export SETTINGS="config.DevelopmentConfig"

py.test --cov-report term-missing --cov application tests
