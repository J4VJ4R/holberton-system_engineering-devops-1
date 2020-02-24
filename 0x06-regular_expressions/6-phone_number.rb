#!/usr/bin/env ruby
name = ARGV[0]
my_name = name.scan(/^\d{10}$/).join
puts "#{my_name}"
