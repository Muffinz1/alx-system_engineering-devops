# installing the flask package @ 2.1.0
# installing the Werkzeug 2.1.1 too

package{'flask':
ensure   =>'2.1.0',
provider =>'pip3',
}
package{'Werkzeug':
ensure   =>'2.1.1',
provider =>'pip3',
}
