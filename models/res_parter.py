from odoo import models, fields


class ResPartner (models.Model):
    _inherit="res.partner"
    
    dogs_ids = fields.One2many('dog.dog', 'partner_id', string='Perros')
    
    
    def action_view_dogs(self):
        action = self.env['ir.actions.act_window']._for_xml_id('dog.parner_dogs')
        action['domain'] = [('partner_id.id','=', self.id)]
        return action