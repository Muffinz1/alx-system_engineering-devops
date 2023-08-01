# Regular expression

## Context

* building my regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. 

## scripts

	* 0. Simply matching School
	* 1. Repetition Token #0
	* 2. Repetition Token #1
	* 3. Repetition Token #2
	* 4. Repetition Token #3
	* 5. Not quite HBTN yet
	* 6. Call me maybe
	* 7. OMG WHY ARE YOU SHOUTING?
## script used

```ruby
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a

```

* The first line of all the  Bash scripts starts 
```bash 
#!/usr/bin/env ruby
```
