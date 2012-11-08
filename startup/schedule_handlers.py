# ERPNext - web based ERP (http://erpnext.com)
# Copyright (C) 2012 Web Notes Technologies Pvt Ltd
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals
"""will be called by scheduler"""

import webnotes
from webnotes.utils import scheduler
	
def execute_all():	
	# bulk email
	from webnotes.utils.email_lib.bulk import flush
	run_fn(flush)
	
def execute_every_ten_minutes():
	# pull emails
	from utilities.doctype.communication.import_emails import import_emails
	run_fn(import_emails)
	
def execute_daily():
	# email digest
	from setup.doctype.email_digest.email_digest import send
	run_fn(send)

	# run recurring invoices
	from accounts.doctype.gl_control.gl_control import manage_recurring_invoices
	run_fn(manage_recurring_invoices)

	# send bulk emails
	from webnotes.utils.email_lib.bulk import clear_outbox
	run_fn(clear_outbox)

def execute_weekly():
	pass

def execute_monthly():
	pass

def execute_hourly():
	pass
	
def run_fn(fn):
	try:
		fn()
	except Exception, e:
		scheduler.log(fn.func_name)
