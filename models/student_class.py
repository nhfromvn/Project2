from odoo import models, fields, api


class StudentClass(models.Model):
    _name = 'student.class'
    name = fields.Char()
    size = fields.Integer(compute='_compute_size')
    teacher = fields.Many2one('teacher')
    students = fields.One2many('student', 'student_class')

    @api.depends('students')
    def _compute_size(self):
        for _class in self:
            _class.size = len(_class.students)
