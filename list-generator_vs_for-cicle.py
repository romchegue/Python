L = [['3', 'Avaya_control_A', 'active'], ['4', 'Avaya_control_B', 'active'], ['5', 'Avaya_voice', 'active'], ['6', 'Avaya_phone', 'active'], ['60', 'MGMT_ALTF', 'active', 'Gi3/0/8,', 'Gi4/0/8'], ['78', 'UIB', 'active'], ['100', 'Video_recorder', 'active'], ['128', 'Srv_ALTF', 'active'], ['129', 'Srv_ALTF1', 'active'], ['132', 'Audit', 'active'], ['264', 'User_ALTF2', 'active'], ['453', 'BB_RTR2-Core', 'active', 'Gi3/0/1'], ['454', 'BB_RTR1-Core', 'active', 'Gi4/0/2'], ['455', 'BB_RTR2-ASA', 'active', 'Gi3/0/19,', 'Gi4/0/19,', 'Gi4/0/22'], ['456', 'BB_RTR1-ASA', 'active', 'Gi3/0/15,', 'Gi3/0/22,', 'Gi4/0/15'], ['457', 'Ch_to_GO_ReTN.net', 'active', 'Gi3/0/20,', 'Gi4/0/20,', 'Gi4/0/21'], ['458', 'Ch_to_GO_BEELINE', 'active', 'Gi3/0/17,', 'Gi3/0/21,', 'Gi4/0/17'], ['461', 'BB_UIB', 'active', 'Gi3/0/16']]
L1 = [['4', 'up', 'up', 'Avaya_Control_B'], ['5', 'up', 'up', 'Avaya_voice'], ['6', 'up', 'up', 'Avaya_phone'], ['60', 'up', 'up', 'MGMT_ALTF'], ['100', 'up', 'up', 'Video_recorder'], ['128', 'up', 'up', 'COMMON_SRV'], ['129', 'up', 'up', 'Alt_Users'], ['132', 'up', 'up', 'Auditors'], ['264', 'up', 'up', 'Alt_Users_(static)'], ['450', 'down', 'down'], ['453', 'up', 'up', 'BB_RTR2-Core_(to_RCHD)'], ['454', 'up', 'up', 'BB_RTR1-Core_(to_RCHD)'], ['461', 'up', 'up', 'BB_IB']]

'''
| This is a generator of a list:

'''
L2 = ['interface vlan {0}\ndescription {1}\n'.format(L[i][0], L[i][1]) for (i, j) in enumerate(L) for (k, l) in enumerate(L1) if L[i][0] == L1[k][0]]

'''
| This is a cickle 'for' for creation of a list:

'''
L2 = []
for (i, j) in enumerate(L):
    for (k, l) in enumerate(L1):
        if L[i][0] == L1[k][0]:
            L2.append('intarface vlan {0}\ndescription {1}\n'.format(L[i][0], L[i][1]))


