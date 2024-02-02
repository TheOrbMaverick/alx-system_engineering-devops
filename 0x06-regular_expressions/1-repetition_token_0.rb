#!/usr/bin/env ruby

# Check if the argument is provided
if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <text>"
  exit 1
end

# Get the argument
text = ARGV[0]

# Regular expression to match the specified cases
regexp = /hbt+n/

# Use scan method to find matches and join the results
puts text.scan(regexp).join
