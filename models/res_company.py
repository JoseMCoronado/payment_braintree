# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ResCompany(models.Model):
    _inherit = "res.company"

    braintree_merchant_id = fields.Char('Merchant Id')
    braintree_public_key = fields.Char('Public Key')
    braintree_private_key = fields.Char('Private Key')
