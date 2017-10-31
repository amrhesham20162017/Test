# -*- coding: utf-8 -*-

from openerp import models, fields,api

class training(models.Model):
    # _name = 'training.training'
    _inherit = "sale.order"

    name_id = fields.Char()
    test = fields.Float(string="",  required=True, )
    test_1 = fields.Float(string="",  required=False )
    date = fields.Date(string="", required=False, )
    datetime = fields.Datetime(string="", required=False, )
    boolean = fields.Boolean(string="",  )
    product = fields.Many2one(comodel_name="product.product", string="", required=False, )
    # donot forget in the field of O2M to write the the name of the other model and the inverse
    tree = fields.One2many(comodel_name="test.test", inverse_name="inverse", string="Amr")

    # @api.depends("test_1")
    # def test_fun(self):
    #     self.test = self.test_1 * 10

    @api.one
    @api.onchange('product')
    def compute_shifts(self):
        x = self.env['product.product'].search([('uom_id', '=', self.product.uom_id.id)])

        for v in x:
            print "=====================================", v.name


    # @api.onchange("product")
    # def test_onchange(self):
    #     print "======================================"
    #     self.test = self.test_1 * 5

class NewModule(models.Model):
    _name = 'test.test'

    username = fields.Char()
    inverse = fields.Many2one(comodel_name="sale.order" )
    salary = fields.Float(string="Salary",  required=False, )
