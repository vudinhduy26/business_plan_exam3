from odoo import api, fields, models
from odoo.exceptions import ValidationError


class SuccessMessage(models.TransientModel):
    _name = 'message.wizard'

    message = fields.Text(string='Message', required=True, readonly=True, store=True)

    def action_ok(self):
        """ close wizard"""
        return {'type': 'ir.actions.act_window_close'}
