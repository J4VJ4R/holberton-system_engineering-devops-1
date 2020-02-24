#!/usr/bin/env ruby
line = ARGV[0]
sender = line.scan /(\[from:(.?\d*|.?\w*)\])/
receiver = line.scan /(\[to:(.?\d*|.?\w*)\])/
flags = line.scan /(flags:((:*-*\d+)*))/
puts "#{sender[0][1]},#{receiver[0][1]},#{flags[0][1]}"
