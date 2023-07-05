# -*- coding: utf-8 -*-
from odoo import http, fields
from odoo.http import request
import jinja2
import os
import json
from datetime import datetime

path = os.path.realpath(os.path.join(os.path.dirname(__file__), '../static/src/html'))
loader = jinja2.FileSystemLoader(path)
jinja_env = jinja2.Environment(loader=loader, autoescape=True)
jinja_env.filters["json"] = json.dumps


class Thpt(http.Controller):
    @http.route('/thpt', auth='user')
    def index(self, **kw):
        user = request.env.user
        if user.role == 'student':
            list_class_student = []
            list_schedule_student = []
            student = request.env['student'].sudo().search([('user', '=', user.id)], limit=1)
            schedules = request.env['schedule'].sudo().search(
                [('student_class', '=', student.student_class.id)])
            for schedule in schedules:
                list_schedule_student.append({
                    'id': schedule.id,
                    'class_time': schedule.class_time,
                    'subject': schedule.subject,
                    'date_of_week': schedule.date_of_week + 1,
                    'semester': schedule.semester,
                    'classroom': schedule.classroom,
                })

            for sstudent in student.student_class.students:
                list_class_student.append({
                    'first_name': sstudent.first_name,
                    'middle_name': sstudent.middle_name if sstudent.middle_name else '',
                    'last_name': sstudent.last_name,
                    'gender': {'value': 'true' if sstudent.gender else 'false',
                               'name': 'Nam' if sstudent.gender else 'Nữ'},
                    'dob': sstudent.dob.strftime('%Y-%m-%d') if sstudent.dob else None,
                    'ethnicity': sstudent.ethnicity,
                    'religion': sstudent.religion,
                    'phone': sstudent.phone,
                    'address': sstudent.address,
                })
            return request.render('thpt.index', {'data': {
                'role': user.role,
                'user_id': user.id,
                'name': f"{student.first_name} {student.middle_name} {student.last_name}",
                'id': student.id,
                'first_name': student.first_name,
                'middle_name': student.middle_name if student.middle_name else '',
                'last_name': student.last_name,
                '_class': {'name': student.student_class.name,
                           'id': student.student_class.id,
                           'teacher': student.student_class.teacher.first_name + ' ' + student.student_class.teacher.middle_name + ' ' + student.student_class.teacher.last_name,

                           },
                'gender': {'value': 'true' if student.gender else 'false',
                           'name': 'Nam' if student.gender else 'Nữ'},
                'dob': student.dob.strftime('%Y-%m-%d') if student.dob else None,
                'ethnicity': student.ethnicity,
                'religion': student.religion,
                'phone': student.phone,
                'address': student.address,
                'list_class_student': list_class_student,
                'image_url': student.image_url,
                'list_schedule_student': list_schedule_student
            }})
        elif user.role == 'teacher':
            teacher = request.env['teacher'].sudo().search([('user', '=', user.id)], limit=1)
            return request.render('thpt.index', {'data': {
                'role': user.role,
                'user_id': user.id,
                'name': f"{teacher.first_name} {teacher.middle_name} {teacher.last_name}",
                'id': teacher.id,
                'first_name': teacher.first_name,
                'middle_name': teacher.middle_name if teacher.middle_name else '',
                'last_name': teacher.last_name,
                'gender': {'value': 'true' if teacher.gender else 'false',
                           'name': 'Nam' if teacher.gender else 'Nữ'},
                'dob': teacher.dob.strftime('%Y-%m-%d') if teacher.dob else None,
                'ethnicity': teacher.ethnicity,
                'religion': teacher.religion,
                'phone': teacher.phone,
                'address': teacher.address,
                'literacy': teacher.literacy,
                'image_url': teacher.image_url
            }})
        elif user.role == 'cadre':
            cadre = request.env['cadre'].sudo().search([('user', '=', user.id)], limit=1)
            print(cadre)
            return request.render('thpt.index', {'data': {
                'role': user.role,
                'user_id': user.id,
                'name': f"{cadre.first_name} {cadre.middle_name} {cadre.last_name}",
                'id': cadre.id,
                'first_name': cadre.first_name,
                'middle_name': cadre.middle_name if cadre.middle_name else '',
                'last_name': cadre.last_name,
                'gender': {'value': 'true' if cadre.gender else 'false',
                           'name': 'Nam' if cadre.gender else 'Nữ'},
                'dob': cadre.dob.strftime('%Y-%m-%d') if cadre.dob else None,
                'ethnicity': cadre.ethnicity,
                'religion': cadre.religion,
                'phone': cadre.phone,
                'address': cadre.address,
                'literacy': cadre.literacy,
                'image_url': cadre.image_url

            }})
        else:
            return request.render('thpt.index', {'data': 'admin'})

    @http.route('/thpt/get/data', auth='user')
    def get_data(self, **kw):
        list_schedule = []
        list_student = []
        list_class = []
        list_teacher = []
        schedules = request.env['schedule'].sudo().search([])
        students = request.env['student'].sudo().search([])
        classes = request.env['student.class'].sudo().search([])
        teachers = request.env['teacher'].sudo().search([])
        for schedule in schedules:
            list_schedule.append({
                'id': schedule.id,
                'class_time': schedule.class_time,
                '_class': {'name': schedule.student_class.name,
                           'id': schedule.student_class.id,
                           'teacher': schedule.student_class.teacher.first_name + ' ' + schedule.student_class.teacher.middle_name + ' ' + schedule.student_class.teacher.last_name,
                           'size': schedule.student_class.size
                           },
                'subject': schedule.subject,
                'teacher': {'id': schedule.teacher.id,
                            'name':
                                schedule.teacher.first_name + ' ' + schedule.teacher.middle_name + ' ' + schedule.teacher.last_name},
                'date_of_week': schedule.date_of_week + 1,
                'semester': schedule.semester,
                'classroom': schedule.classroom,
            })
        for student in students:
            list_student.append({
                'id': student.id,
                'first_name': student.first_name,
                'middle_name': student.middle_name if student.middle_name else '',
                'last_name': student.last_name,
                '_class': {'name': student.student_class.name,
                           'id': student.student_class.id,
                           'teacher': student.student_class.teacher.first_name + ' ' + student.student_class.teacher.middle_name + ' ' + student.student_class.teacher.last_name,
                           'size': student.student_class.size
                           } if student.student_class else None,
                'gender': {'value': student.gender,
                           'name': 'Nam' if student.gender else 'Nữ'},
                'dob': student.dob.strftime('%Y-%m-%d') if student.dob else None,
                'ethnicity': student.ethnicity,
                'religion': student.religion,
                'phone': student.phone,
                'address': student.address,
            }),
        for sclass in classes:
            list_class.append({
                'id': sclass.id,
                'name': sclass.name,
                'teacher': sclass.teacher.first_name + ' ' + sclass.teacher.middle_name + ' ' + sclass.teacher.last_name,
                'size': sclass.size
            })
        for teacher in teachers:
            list_subject = []
            for subject in teacher.office_subject:
                list_subject.append({
                    'name': subject.name,
                    'office': subject.office,
                    'num_teacher': subject.num_teacher
                })
            list_teacher.append({
                'id': teacher.id,
                'first_name': teacher.first_name,
                'middle_name': teacher.middle_name,
                'last_name': teacher.last_name,
                'working_time': teacher.working_time,
                'subjects': list_subject,
                'gender': {'value': teacher.gender,
                           'name': 'Nam' if teacher.gender else 'Nu'},
                '_class': {'name': student.student_class.name,
                           'id': student.student_class.id,
                           'teacher': student.student_class.teacher.first_name + ' ' + student.student_class.teacher.middle_name + ' ' + student.student_class.teacher.last_name,
                           'size': student.student_class.size
                           },
                'dob': teacher.dob.strftime('%Y-%m-%d') if student.dob else None,
                'ethnicity': teacher.ethnicity,
                'religion': teacher.religion,
                'phone': teacher.phone,
                'address': teacher.address,
                'literacy': teacher.literacy,
                'main_teacher': teacher.main_teacher
            })

        return json.dumps({'students': list_student,
                           'classes': list_class,
                           'teachers': list_teacher,
                           'schedules': list_schedule})

    @http.route('/thpt/add/student', type='json', auth='user')
    def add_student(self, **kw):
        res = json.loads(request.httprequest.data)
        student = request.env['student'].sudo().create({
            'first_name': res['first_name'],
            'middle_name': res['middle_name'],
            'last_name': res['last_name'],
            'gender': res['gender']['value'],
            'dob': datetime.strptime(res['dob'], '%Y-%m-%d'),
            'address': res['address'],
            'religion': res['religion'],
            'ethnicity': res['ethnicity'],
            'phone': res['phone'],
            'student_class': request.env['student.class'].sudo().search([('name', '=', res['_class']['name'])],
                                                                        limit=1).id
        })
        res['id'] = student.id
        return res

    @http.route('/thpt/save/student', type='json', auth='user')
    def change_student(self, **kw):
        res = json.loads(request.httprequest.data)
        student = request.env['student'].sudo().search([('id', '=', res['id'])])
        student.write({
            'first_name': res['first_name'],
            'middle_name': res['middle_name'],
            'last_name': res['last_name'],
            'gender': res['gender']['value'],
            'dob': datetime.strptime(res['dob'], '%Y-%m-%d'),
            'address': res['address'],
            'religion': res['religion'],
            'ethnicity': res['ethnicity'],
            'phone': res['phone'],
            'student_class': request.env['student.class'].sudo().search([('name', '=', res['_class']['name'])],
                                                                        limit=1).id
        })

        return res

    @http.route('/thpt/add/schedule', type='json', auth='user')
    def add_schedule(self, **kw):
        res = json.loads(request.httprequest.data)
        schedule = request.env['schedule'].sudo().create({
            'student_class': request.env['student.class'].sudo().search([('name', '=', res['_class']['name'])],
                                                                        limit=1).id,
            'date_of_week': res['date_of_week'] - 1,
            'subject': res['subject'],
            'semester': res['semester'],
            'teacher': request.env['teacher'].sudo().search([('id', '=', res['teacher']['id'])],
                                                            limit=1).id,
            'classroom': res['classroom'],
            'class_time': res['class_time'],
        })
        res['id'] = schedule.id
        return res

    @http.route('/thpt/save/schedule', type='json', auth='user')
    def change_schedule(self, **kw):
        res = json.loads(request.httprequest.data)
        schedule = request.env['schedule'].sudo().search([('id', '=', res['id'])])
        schedule.write({
            'student_class': request.env['student.class'].sudo().search([('name', '=', res['_class']['name'])],
                                                                        limit=1).id,
            'date_of_week': res['date_of_week'] - 1,
            'subject': res['subject'],
            'semester': res['semester'],
            'teacher': request.env['teacher'].sudo().search([('id', '=', res['teacher']['id'])],
                                                            limit=1).id,
            'classroom': res['classroom'],
            'class_time': res['class_time'],
        })

        return res

    @http.route('/thpt/add/teacher', type='json', auth='user')
    def add_teacher(self, **kw):
        res = json.loads(request.httprequest.data)
        teacher = request.env['teacher'].sudo().create({
            'first_name': res['first_name'],
            'middle_name': res['middle_name'],
            'last_name': res['last_name'],
            'gender': res['gender']['value'],
            'dob': datetime.strptime(res['dob'], '%Y-%m-%d'),
            'address': res['address'],
            'religion': res['religion'],
            'ethnicity': res['ethnicity'],
            'phone': res['phone'],
            'literacy': res['literacy'],
            'main_teacher': res['main_teacher'],
            'student_class': request.env['student.class'].sudo().search([('name', '=', res['_class']['name'])],
                                                                        limit=1).id if res['main_teacher'] else None
        })
        res['id'] = teacher.id
        return res

    @http.route('/thpt/save/teacher', type='json', auth='user')
    def change_teacher(self, **kw):
        res = json.loads(request.httprequest.data)
        teacher = request.env['teacher'].sudo().search([('id', '=', res['id'])])
        teacher.write({
            'first_name': res['first_name'],
            'middle_name': res['middle_name'],
            'last_name': res['last_name'],
            'gender': res['gender']['value'],
            'dob': datetime.strptime(res['dob'], '%Y-%m-%d'),
            'address': res['address'],
            'religion': res['religion'],
            'ethnicity': res['ethnicity'],
            'phone': res['phone'],
            'literacy': res['literacy'],
            'main_teacher': res['main_teacher'],
            'student_class': request.env['student.class'].sudo().search([('name', '=', res['_class']['name'])],
                                                                        limit=1).id if res['main_teacher'] else None
        })

        return res
