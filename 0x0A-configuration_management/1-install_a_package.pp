#!/usr/bin/pup
# installing the flask package @ 2.1.0

package {'flask':
ensure   =>'2.1.0',
provider =>'pip3',
}
