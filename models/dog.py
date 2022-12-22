from odoo import models, fields, api
from datetime import date


class Dog (models.Model):
    _name = "dog.dog"

    name = fields.Char('Nombre', required=True)
    date_of_birth = fields.Date('Fecha de nacimiento', required=True)
    
    microchip = fields.Integer('Microchip')
    retired = fields.Boolean('Retirado')
    RFEC = fields.Boolean('RFEC')
    numero_liencica_RFEC = fields.Integer('Numero liencicaRFEC')
    jump_height_RFEC = fields.Selection([
        ('20', '20'),
        ('30', '30'),
        ('40', '40'),
        ('50', '50'),
        ('60', '60'),
    ], string='Altura de salto RFEC')
    
    RSCE = fields.Boolean('RSCE')
    numero_liencica_RSCE = fields.Integer('Numero liencica RSCE')
    jump_height_RSCE = fields.Selection([
        ('xmall', 'xmall'),
        ('small', 'small'),
        ('medium', 'medium'),
        ('intermediate', 'intermediate'),
        ('large', 'large'),
    ], string='Altura de salto RFEC')
    
    
    partner_id = fields.Many2one('res.partner', string='Dueño')
    
    
    points_ids = fields.One2many('dog.points', 'dog_id', string='Puntos')
    
    def action_view_points(self):
        action = self.env['ir.actions.act_window']._for_xml_id('dog.dog_points_action')
        action['domain'] = [('dog_id.id','=', self.id)]
        return action

    
    age = fields.Char('Edad', compute="_calculate_age", default=0)
    
    @api.onchange('date_of_birth')
    def _calculate_age(self):
         for record in self:
            if record.date_of_birth != False:
                today = date.today()
                edad = (today - record.date_of_birth).days
                month = edad / 31
                record.age = "{}".format(int(month)) + " meses"