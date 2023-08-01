#!/usr/bin/env ruby

sender = ARGV[0].scan(/from:(.*?)\]/)
reciever = ARGV[0].scan(/to:(.*?)\]/)
flags = ARGV[0].scan(/flags:(.*?)\]/)

puts [sender, reciever, flags].join(",")
