# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Management System - Audit",
    "version": "1.2",
    "author": "Savoir-faire Linux",
    "website": "http://www.savoirfairelinux.com",
    "license": "AGPL-3",
    "category": "Management System",
    "description": """\
This module enables you to manage audits and verifications lists of your
management system.
    """,
    "depends": ['mgmtsystem_nonconformity'],
    "data": [
        'security/ir.model.access.csv',
        'security/mgmtsystem_audit_security.xml',
        'data/ir_sequence_type.xml',
        'data/ir_sequence.xml',
        'data/ir_actions_server.xml',
        'data/base_action_rule.xml',
        'views/mgmtsystem_verification_line.xml',
        'views/mgmtsystem_audit.xml',
        'views/mgmtsystem_nonconformity.xml',
        'views/board_board.xml',
        'report/audit_report.xml',
        'report/verification_list.xml',
        'wizard/copy_verification_lines.xml',
    ],
    "demo": [
        'demo/mgmtsystem_audit.xml',
    ],
    "installable": True,
}
