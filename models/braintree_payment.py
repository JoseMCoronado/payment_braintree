# coding: utf-8

import logging
import braintree
import json

from odoo import api, fields, models, _
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

class braintree_payment_sale_wizard(models.TransientModel):
    _name = "braintree.payment.sale.wizard"
    _description = 'Braintree Payment Wizard from Sale Order'

    sale_id = fields.Many2one('sale.order',string='Sale Order')
    credit_card_num = fields.Char('Credit Card Number')
    expiration_month = fields.Selection([
        ('01', '01'),
        ('02', '02'),
        ('03', '03'),
        ('04', '04'),
        ('05', '05'),
        ('06', '06'),
        ('07', '07'),
        ('08', '08'),
        ('09', '09'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ], string='Expiration Month')
    expiration_year = fields.Char('Expiration Year', placeholder='e.g. 2020')
    cvv = fields.Char('CVV')
    amount = fields.Float('Amount')

    @api.multi
    def create_payment(self):
        for payment in self:
            company = rate.env['res.users'].browse([rate.env.uid]).company_id
            if not company.braintree_merchant_id or not company.braintree_public_key or not company.braintree_private_key:
                 raise UserError('Missing Braintree API Credentials. Please set up in the company configuration form.')
            braintree.Configuration.configure(braintree.Environment.Sandbox,
                                              merchant_id=company.braintree_merchant_id,
                                              public_key=company.braintree_public_key,
                                              private_key=company.braintree_private_key)

            result = braintree.Transaction.sale({
                "credit_card": {
                    "number": payment.credit_card_num,
                    "expiration_date": payment.expiration_month+"/"+payment.expiration_year,
                    "cvv": payment.cvv
                },
                "amount": str(payment.amount),
                "options": {
                    "submit_for_settlement": "true"
                }
            })

            if result.is_success:
                transaction = result.transaction
                raise UserError("""
                    Payment successfully captured
                    Transaction ID: %s
                    """ % (transaction.id))
            else:
                raise UserError(result.message)
