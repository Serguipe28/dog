from odoo import models, fields


class Club(models.Model): 
    _name = "dog.club"
    
    
    name = fields.Char('Nombre')
    ubi = fields.Char('Ubicacion')