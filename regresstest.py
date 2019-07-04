# file: regresstest.py

import os, sys
print(sys.argv)   # Просто для теста
testscripts = [dict(script='comma-sep-summator.py', args='data.txt 3'), # Или подставьте свои
               dict(script='nextexc.py', args='')]                      # значения script/args

for testcase in testscripts:
    commandline = '{executer} {script} {args}'.format(executer=sys.executable, **testcase)
    output = os.popen(commandline).read()
    result = testcase['script'] + '.result'
    if not os.path.exists(result):
        open(result, 'w').write(output)
        print('Created:', result)
    else:
        priorresult = open(result).read()
        if output != priorresult:
            print('FAILED:', testcase['script'])
        else:
            print('Passed:', testcase['script'])

