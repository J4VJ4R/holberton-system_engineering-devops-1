#!/usr/bin/env ruby
line = ARGV[0]
# sender = line.scan /(\[from:(.?\d*|.?\w*)\])/
# receiver = line.scan /(\[to:(.?\d*|.?\w*)\])/
# flags = line.scan /(flags:((:*-*\d+)*))/
# puts "#{sender[0][1]},#{receiver[0][1]},#{flags[0][1]}"
sender = line.scan /(?<=from:).+?(?=\])/
receiver = line.scan /(?<=to:).+?(?=\])/
flags = line.scan /(?<=flags:).+?(?=\])/
puts "#{sender[0]},#{receiver[0]},#{flags[0]}"
