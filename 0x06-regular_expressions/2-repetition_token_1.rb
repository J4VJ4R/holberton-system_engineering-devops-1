#!/usr/bin/env ruby
name = ARGV[0]
my_name = name.scan(/hb{0,1}tn/).join
puts "#{my_name}"
