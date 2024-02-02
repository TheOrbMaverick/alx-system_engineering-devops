#!/usr/bin/env ruby

# Check if the argument is provided
if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <text>"
  exit 1
end

# Get the argument
text = ARGV[0]

# Regular expression to match only capital letters
regexp = /[A-Z]/

# Use scan method to find matches and join the results
shouted_text = text.scan(regexp).join

# Print the result if there are matches, otherwise print an empty line
puts shouted_text.empty? ? "$" : shouted_text
