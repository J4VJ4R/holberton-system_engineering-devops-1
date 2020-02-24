#!/usr/bin/env ruby
name = ARGV[0]
my_name = name.scan(/[A-Z]*/).join
puts "#{my_name}"
