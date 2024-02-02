#!/usr/bin/env ruby

# Check if the argument is provided
if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <log_entry>"
  exit 1
end

# Get the log entry from the command line argument
log_entry = ARGV[0]

# Regular expression to extract relevant information from the log entry
regexp = /\[from:([^ \]]+)\] \[to:([^ \]]+)\] \[flags:([^ \]]+)\]/

# Use match method to extract matches from the log entry
matches = log_entry.match(regexp)

# Check if there are matches
if matches
  sender = matches[1]
  receiver = matches[2]
  flags = matches[3]

  # Output the result in the required format
  puts "#{sender},#{receiver},#{flags}"
else
  # Output an empty line if no matches are found
  puts ""
end
