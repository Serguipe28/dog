from odoo import models, fields



class Point(models.Model):
    _name="dog.points"
    
    
    dog_id = fields.Many2one('dog.dog', string='Perro')
    guia = fields.Char('Guia', related='dog_id.partner_id.name')
    club_id = fields.Many2one('dog.club', string='Club')
    federacion = fields.Selection([
        ('RSCE', 'RSCE'),
        ('RFEC', 'RFEC')
    ], string='Federacion')
    tipo = fields.Selection([
        ('Agility', 'Agility'),
        ('Jumping', 'Jumping')
    ], string='Tipo')
    date = fields.Date('Fecha')   
    speed = fields.Float('Velocidad (m/s)') 