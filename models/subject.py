from odoo import models, fields, api


class Subject(models.Model):
    _name = 'subject'
    name = fields.Char()
    teacher = fields.Many2one('teacher')
    student = fields.Many2one('student')
    subject_infos = fields.One2many('subject.info', 'subject')
    average_score = fields.Float(compute='_compute_average')

    @api.depends('subject_infos')
    def _compute_average(self):
        for subject in self:
            count = 0
            sum = 0
            if subject.subject_infos:
                for subject_info in subject.subject_infos:
                    sum += subject_info.score * subject_info.multiplier
                    count += subject_info.multiplier
                subject.average_score = sum / count
            else:
                subject.average_score = 0
