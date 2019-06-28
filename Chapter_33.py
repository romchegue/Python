class Tester:
    tester_counter = 1   # Counts a number of calls of method Tester.tester
    def tester():
        """
        Method Tester.tester() prompts you to enter an expression
        and then displays the result of the expression
        """	
        x = input('{0}. Input an expression:\n'.format(Tester.tester_counter))
        try:
            print('\nThe result: {0}'.format(eval(x)))
        except (TypeError):
            print('\nTypeError\n')
        except (ValueError):
            print('\nValueError\n')
        except (IndexError):
            print('\nIndexError\n')
        except (ZeroDivisionError):
            print('\nZeroDivisionError\n')		
        except Exception as value:
            print('\nException: {0}\n'.format(value))
        finally:
            print('- - - - -\n')
            Tester.tester_counter +=1
            Tester.tester()
    def printer_with_timer(string='_', fact=1, slp=1):
        """
        Method Tester.printer_with_timer(string='_', fact=1, slp=1)
        prints text from argument named string starting with
        fact repetitions with pauses slp
        """
        import time
        while fact:
            try:
                print(string * fact)
                fact += 1
                time.sleep(slp)
            except KeyboardInterrupt:         # You should press Ctrl+C to interrupt this cycle
                flag = input('\nDO YOU REALLY WANT TO QUIT? (y/...')    # But you can continue by press 'Y/y/yes/YES/Yes/Yep etc'
                if flag.lower()[:1] == 'y': 
                    fact = 0
        else:
            print('\nGOOD BYE!!!\n')



try:
    5/0
except ZeroDivisionError as value:
    print('\nZeroDivisionError: {0}\n'.format(type(value)))
    input('PRESS ENTER FOR EXIT ')
    exit()
finally:
    print('GOOOOOOOD BYE!!!')


class TraceBlock:
    def message(self, arg):
        print('running', arg)
    def __enter__(self):
        print('starting with block')
        return self
    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print('excited normally\n')
        else:
            print('raise an exception!', exc_type)
            return False

with TraceBlock() as action:
    action.message('test 1')
    print('reached')

with TraceBlock() as action:
    action.message('test 2')
    raise TypeError
    print('not reached')













        

