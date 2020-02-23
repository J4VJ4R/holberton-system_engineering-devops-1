#!/usr/bin/env ruby
name = ARGV[0]
my_name = name.scan(/Holberton/).join
puts "#{my_name}"
