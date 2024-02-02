#!/usr/bin/env ruby

# Check if the argument is provided
if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <phone_number>"
  exit 1
end

# Get the argument
phone_number = ARGV[0]

# Regular expression to match a 10-digit phone number
regexp = /^\d{10}$/

# Check if the phone number matches the pattern
if phone_number.match?(regexp)
  puts "#{phone_number}$"
else
  puts "$"
end
