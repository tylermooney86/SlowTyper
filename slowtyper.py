import sys,time,random,argparse

def slow_type(t,typing_speed = 100):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*5.0/typing_speed)
    print ('')

def display_ascii(filename,typing_speed=100):
	file = open(filename,'r')
	output = file.read()
	slow_type(output,typing_speed)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Data Mining HW2')
    parser.add_argument('-f', type=str,
                            help="Location of filename",
                            required=True)
    parser.add_argument("-s", type=int, 
                            help="Speed of simulated typing",
                            required=False)

    args = parser.parse_args()

    if ( args.f and args.s ):
        display_ascii( args.f , args.s)
    elif ( args.f ):
        display_ascii( args.f )
    else:
        print ("Kindly provide input of the following form:\nslowtyper.py -f <filename> -s <integer>")