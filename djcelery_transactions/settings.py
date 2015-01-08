# -*- coding: utf-8 -*-
'''
Created on Jan 8, 2015

@author: jakob
'''
from django.conf import settings

# Whether or not to execute tasks on savepoint commits
EXEC_ON_SAVEPOINT = getattr(settings, 'DJCELERY_TRANSACTIONS_EXEC_ON_SAVEPOINT', True)