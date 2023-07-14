# -*- coding: utf-8 -*-
from odoo import http, fields
from odoo.http import request
import jinja2
import os
import json
from datetime import datetime
import random

path = os.path.realpath(os.path.join(os.path.dirname(__file__), '../static/src/html'))
loader = jinja2.FileSystemLoader(path)
jinja_env = jinja2.Environment(loader=loader, autoescape=True)
jinja_env.filters["json"] = json.dumps


class Thpt(http.Controller):
    @http.route('/thpt', auth='user')
    def index(self, **kw):
        user = request.env.user
        activities = request.env['extracurricular.activities'].sudo().search([])
        list_activity = []
        for extracurricular_activitie in activities:
            list_id = []
            for participant in extracurricular_activitie.participants:
                list_id.append(participant.id)
            list_activity.append({
                'id': extracurricular_activitie.id,
                'title': extracurricular_activitie.title,
                'description': extracurricular_activitie.description,
                'teacher_in_charge': {'id': extracurricular_activitie.teacher_in_charge.id,
                                      'name': extracurricular_activitie.teacher_in_charge.first_name + ' ' + extracurricular_activitie.teacher_in_charge.middle_name + ' ' + extracurricular_activitie.teacher_in_charge.last_name, },
                'time': extracurricular_activitie.time,
                'location': extracurricular_activitie.location,
                'max_participant': extracurricular_activitie.max_participants,
                'semester': extracurricular_activitie.semester,
                'content': extracurricular_activitie.content,
                'start_time': extracurricular_activitie.start_time.strftime(
                    '%Y-%m-%d') if extracurricular_activitie.start_time else None,
                'end_time': extracurricular_activitie.end_time.strftime(
                    '%Y-%m-%d') if extracurricular_activitie.end_time else None,
                'support_teacher1': {'id': extracurricular_activitie.support_teacher1.id,
                                     'name': extracurricular_activitie.support_teacher1.first_name + ' ' + extracurricular_activitie.support_teacher1.middle_name + ' ' + extracurricular_activitie.support_teacher1.last_name, },
                'support_teacher2': {'id': extracurricular_activitie.support_teacher2.id,
                                     'name': extracurricular_activitie.support_teacher2.first_name + ' ' + extracurricular_activitie.support_teacher2.middle_name + ' ' + extracurricular_activitie.support_teacher2.last_name, },
                'support_teacher3': {'id': extracurricular_activitie.support_teacher3.id,
                                     'name': extracurricular_activitie.support_teacher3.first_name + ' ' + extracurricular_activitie.support_teacher3.middle_name + ' ' + extracurricular_activitie.support_teacher3.last_name, },
                'participants': list_id,

            })
        if user.role == 'student':
            list_class_student = []
            list_schedule_student = []
            list_subject = []
            student = request.env['student'].sudo().search([('user', '=', user.id)], limit=1)
            schedules = request.env['schedule'].sudo().search(
                [('student_class', '=', student.student_class.id)])
            subjects = request.env['subject'].sudo().search([('student', '=', student.id)])

            for subject in subjects:
                list_subject_info = []
                for subject_info in subject.subject_infos:
                    list_subject_info.append(
                        {'id': subject_info.id,
                         'semester': subject_info.semester,
                         'score': subject_info.score,
                         'multiplier': subject_info.multiplier,

                         }
                    )
                list_subject.append({
                    'id': subject.id,
                    'name': subject.name,
                    'student': {'id': subject.student.id,
                                'serial': subject.student.serial,
                                '_class': subject.student.student_class.name,
                                'name': f'{subject.student.first_name} {subject.student.middle_name} {subject.student.last_name}'},

                    'teacher': {'id': subject.teacher.id,
                                'name': f'{subject.teacher.first_name} {subject.teacher.middle_name} {subject.teacher.last_name}'},
                    'subject_infos': list_subject_info,
                    'average_score': subject.average_score
                })
            for schedule in schedules:
                list_schedule_student.append({
                    'id': schedule.id,
                    'class_time': schedule.class_time,
                    'subject': schedule.subject if schedule.subject else '',
                    'date_of_week': schedule.date_of_week + 1,
                    'semester': schedule.semester,

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

                           } if student.student_class else None,
                'gender': {'value': 'true' if student.gender else 'false',
                           'name': 'Nam' if student.gender else 'Nữ'},
                'dob': student.dob.strftime('%Y-%m-%d') if student.dob else None,
                'ethnicity': student.ethnicity,
                'religion': student.religion,
                'phone': student.phone,
                'address': student.address,
                'list_class_student': list_class_student,
                'image_url': student.image_url if student.image_url else '/thpt/static/app/img/anh-meo-cute.jpg',
                'list_schedule_student': list_schedule_student,
                'list_subject': list_subject,
                'extracurricular_activities': list_activity
            }})
        elif user.role == 'teacher':

            teacher = request.env['teacher'].sudo().search([('user', '=', user.id)], limit=1)
            subjects = request.env['subject'].sudo().search([('teacher', '=', teacher.id)])
            _class = request.env['student.class'].sudo().search([('teacher', '=', teacher.id)])
            list_schedule_teacher = []
            list_subject = []
            list_class_student = []
            schedules = request.env['schedule'].sudo().search(
                [('teacher', '=', teacher.id)])
            for sstudent in _class.students:
                list_outcome = []
                outcomes = request.env['semester.outcome'].sudo().search([('student', '=', sstudent.id)])
                for outcome in outcomes:
                    list_outcome.append({
                        'id': outcome.id,
                        'conduct': outcome.conduct,
                        'academic_ability': outcome.academic_ability,
                        'semester': outcome.semester
                    })
                list_class_student.append({
                    'id': sstudent.id,
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
                    'list_outcome': list_outcome

                })
            for subject in subjects:
                list_subject_info = []
                for subject_info in subject.subject_infos:
                    list_subject_info.append(
                        {'id': subject_info.id,
                         'semester': subject_info.semester,
                         'score': subject_info.score,
                         'multiplier': subject_info.multiplier,

                         }
                    )
                list_subject.append({
                    'id': subject.id,
                    'name': subject.name,
                    'student': {'id': subject.student.id,
                                'serial': subject.student.serial,
                                '_class': subject.student.student_class.name,
                                'name': f'{subject.student.first_name} {subject.student.middle_name} {subject.student.last_name}'},

                    'teacher': {'id': subject.teacher.id,
                                'name': f'{subject.teacher.first_name} {subject.teacher.middle_name} {subject.teacher.last_name}'},
                    'subject_infos': list_subject_info,
                    'average_score': subject.average_score,
                })
            for schedule in schedules:
                list_schedule_teacher.append({
                    'id': schedule.id,
                    'class_time': schedule.class_time,
                    'subject': schedule.subject if schedule.subject else '',
                    'date_of_week': schedule.date_of_week + 1,
                    'semester': schedule.semester,
                    'class': schedule.student_class.name
                })
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
                'image_url': teacher.image_url if teacher.image_url else '/thpt/static/app/img/anh-meo-cute.jpg',
                'main_teacher': 1 if teacher.main_teacher else 0,
                'subject': teacher.office_subject.name,
                'list_schedule_teacher': list_schedule_teacher,
                'list_subject': list_subject,
                'extracurricular_activities': list_activity,
                'list_class_student': list_class_student
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
                'image_url': cadre.image_url if cadre.image_url else '/thpt/static/app/img/anh-meo-cute.jpg',

                'working_time': cadre.working_time,
                'team_in_charge': cadre.team_in_charge

            }})
        else:
            return request.render('thpt.index', {'data': 'admin'})

    @http.route('/thpt/get/new', auth='user')
    def get_news(self):
        list_news = []
        news = request.env['news'].sudo().search([])
        for new in news:
            list_news.append({
                'id': new.title,
                'title': new.title,
                'description': new.description,
                'content': new.content,
                'start_time': new.start_time.strftime(
                    '%Y-%m-%d') if new.start_time else None,
                'end_time': new.end_time.strftime(
                    '%Y-%m-%d') if new.end_time else None,

            })
        return json.dumps({
            'news': list_news,
        })

    @http.route('/thpt/save/news', type='json', auth='user')
    def save_news(self, **kw):
        res = json.loads(request.httprequest.data)
        if res['id']:
            new = request.env['news'].sudo().search([('id', '=', res['id'])])
            new.write({

                'title': res['title'],
                'description': res['description'],
                'content': res['content'],
                'start_time': datetime.strptime(res['start_time'], '%Y-%m-%d'),
                'end_time': datetime.strptime(res['end_time'], '%Y-%m-%d'),

            })
        else:
            new = request.env['news'].sudo().create({

                'title': res['title'],
                'description': res['description'],
                'content': res['content'],
                'start_time': datetime.strptime(res['start_time'], '%Y-%m-%d'),
                'end_time': datetime.strptime(res['end_time'], '%Y-%m-%d'),

            })
            res['id'] = new.id
        return res

    @http.route('/thpt/get/data', auth='user')
    def get_data(self, **kw):
        list_schedule = []
        list_student = []
        list_class = []
        list_teacher = []
        list_subject = []
        list_news = []
        news = request.env['news'].sudo().search([])
        list_extracurricular_activities = []
        extracurricular_activities = request.env['extracurricular.activities'].sudo().search([])
        subjects = request.env['subject'].sudo().search([])
        schedules = request.env['schedule'].sudo().search([])
        students = request.env['student'].sudo().search([])
        classes = request.env['student.class'].sudo().search([])
        teachers = request.env['teacher'].sudo().search([])
        for new in news:
            list_news.append({
                'id': new.title,
                'title': new.title,
                'description': new.description,
                'content': new.content,
                'start_time': new.start_time.strftime(
                    '%Y-%m-%d') if new.start_time else None,
                'end_time': new.end_time.strftime(
                    '%Y-%m-%d') if new.end_time else None,

            })
        for extracurricular_activitie in extracurricular_activities:
            list_id = []
            for participant in extracurricular_activitie.participants:
                list_id.append(participant.id)
            list_extracurricular_activities.append({
                'id': extracurricular_activitie.id,
                'title': extracurricular_activitie.title,
                'description': extracurricular_activitie.description,
                'teacher_in_charge': {'id': extracurricular_activitie.teacher_in_charge.id,
                                      'name': extracurricular_activitie.teacher_in_charge.first_name + ' ' + extracurricular_activitie.teacher_in_charge.middle_name + ' ' + extracurricular_activitie.teacher_in_charge.last_name, },
                'time': extracurricular_activitie.time,
                'location': extracurricular_activitie.location,
                'max_participant': extracurricular_activitie.max_participants,
                'semester': extracurricular_activitie.semester,
                'content': extracurricular_activitie.content,
                'start_time': extracurricular_activitie.start_time.strftime(
                    '%Y-%m-%d') if extracurricular_activitie.start_time else None,
                'end_time': extracurricular_activitie.end_time.strftime(
                    '%Y-%m-%d') if extracurricular_activitie.end_time else None,
                'support_teacher1': {'id': extracurricular_activitie.support_teacher1.id,
                                     'name': extracurricular_activitie.support_teacher1.first_name + ' ' + extracurricular_activitie.support_teacher1.middle_name + ' ' + extracurricular_activitie.support_teacher1.last_name, },
                'support_teacher2': {'id': extracurricular_activitie.support_teacher2.id,
                                     'name': extracurricular_activitie.support_teacher2.first_name + ' ' + extracurricular_activitie.support_teacher2.middle_name + ' ' + extracurricular_activitie.support_teacher2.last_name, },
                'support_teacher3': {'id': extracurricular_activitie.support_teacher3.id,
                                     'name': extracurricular_activitie.support_teacher3.first_name + ' ' + extracurricular_activitie.support_teacher3.middle_name + ' ' + extracurricular_activitie.support_teacher3.last_name, },
                'participants': list_id,

            })
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
                                schedule.teacher.first_name + ' ' + schedule.teacher.middle_name + ' ' + schedule.teacher.last_name} if schedule.teacher else False,
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
                'teacher': {'id': sclass.teacher.id,
                            'name': sclass.teacher.first_name + ' ' + sclass.teacher.middle_name + ' ' + sclass.teacher.last_name},
                'size': sclass.size
            })
        for teacher in teachers:
            list_teacher.append({
                'id': teacher.id,
                'first_name': teacher.first_name,
                'middle_name': teacher.middle_name,
                'last_name': teacher.last_name,
                'working_time': teacher.working_time,
                'subject': teacher.office_subject.name,
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
        for subject in subjects:
            list_subject_info = []
            for subject_info in subject.subject_infos:
                list_subject_info.append(
                    {'id': subject_info.id,
                     'semester': subject_info.semester,
                     'score': subject_info.score,
                     'multiplier': subject_info.multiplier,
                     }
                )
            list_subject.append({
                'id': subject.id,
                'name': subject.name,
                'student': {'id': subject.student.id,
                            'serial': subject.student.serial,
                            '_class': subject.student.student_class.name,
                            'name': f'{subject.student.first_name} {subject.student.middle_name} {subject.student.last_name}'},

                'teacher': {'id': subject.teacher.id,
                            'name': f'{subject.teacher.first_name} {subject.teacher.middle_name} {subject.teacher.last_name}'},
                'subject_infos': list_subject_info,
                'average_score': subject.average_score
            })
        return json.dumps({'students': list_student,
                           'classes': list_class,
                           'teachers': list_teacher,
                           'schedules': list_schedule,
                           'subjects': list_subject,
                           'extracurricular_activities': list_extracurricular_activities,
                           'news': list_news
                           })

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
        for i in range(1, 3):
            outcomes = request.env['semester.outcome'].sudo().search(
                [('student', '=', student.id), ('semester', '=', i)])
            if len(outcomes) < 2:
                request.env['semester.outcome'].sudo().create({
                    'student': student.id,
                    'semester': i,
                    'conduct': 'Tốt',
                    'academic_ability': 'Giỏi'
                })
        for subject in ['Toán', 'Vật lý', 'Hóa học', 'Sinh học', 'Văn', 'Lịch sử', 'Địa lý', 'Giáo dục công dân',
                        'Công nghệ', 'Tin học', 'Tiếng anh', 'Thể dục']:
            subject_exist = request.env['subject'].sudo().search([('name', '=', subject), ('student', '=', student.id)])
            if not subject_exist:
                office_id = request.env['office.subject'].sudo().search([('name', '=', subject)], limit=1).id
                subject_exist = request.env['subject'].sudo().create({
                    'name': subject,
                    'student': student.id,
                    'teacher': request.env['teacher'].sudo().search([('office_subject', '=', office_id)], limit=1).id
                })

            if subject_exist:
                for i in range(1, 3):
                    sj_inf = request.env['subject.info'].sudo().search(
                        [('multiplier', '=', 3), ('subject', '=', subject_exist.id), ('semester', '=', i)], limit=1)
                    if not sj_inf:
                        request.env['subject.info'].sudo().create({
                            'subject': subject_exist.id,
                            'score': random.randint(1, 10),
                            'multiplier': 3,
                            'semester': i
                        })
                    for j in range(1, 6):
                        list1 = request.env['subject.info'].sudo().search(
                            [('multiplier', '=', 1), ('subject', '=', subject_exist.id), ('semester', '=', i)])
                        if len(list1) < 5:
                            sj_info1 = request.env['subject.info'].sudo().create({
                                'subject': subject_exist.id,
                                'score': random.randint(1, 10),
                                'multiplier': 1,
                                'semester': i

                            }),
                        list2 = request.env['subject.info'].sudo().search(
                            [('multiplier', '=', 2), ('subject', '=', subject_exist.id), ('semester', '=', i)])
                        if len(list2) < 5:
                            sj_info2 = request.env['subject.info'].sudo().create({
                                'subject': subject_exist.id,
                                'score': random.randint(1, 10),
                                'multiplier': 2,
                                'semester': i
                            })
        return res

    @http.route('/thpt/save/student', type='json', auth='user')
    def change_student(self, **kw):
        res = json.loads(request.httprequest.data)
        student = request.env['student'].sudo().search([('id', '=', res['id'])])
        for i in range(1, 3):
            outcomes = request.env['semester.outcome'].sudo().search(
                [('student', '=', student.id), ('semester', '=', i)])
            if len(outcomes) < 2:
                request.env['semester.outcome'].sudo().create({
                    'student': student.id,
                    'semester': i,
                    'conduct': 'Tốt',
                    'academic_ability': 'Giỏi'
                })
        for subject in ['Toán', 'Vật lý', 'Hóa học', 'Sinh học', 'Văn', 'Lịch sử', 'Địa lý', 'Giáo dục công dân',
                        'Công nghệ', 'Tin học', 'Tiếng anh', 'Thể dục']:
            subject_exist = request.env['subject'].sudo().search([('name', '=', subject), ('student', '=', student.id)])
            if not subject_exist:
                office_id = request.env['office.subject'].sudo().search([('name', '=', subject)], limit=1).id
                subject_exist = request.env['subject'].sudo().create({
                    'name': subject,
                    'student': student.id,
                    'teacher': request.env['teacher'].sudo().search([('office_subject', '=', office_id)], limit=1).id
                })

            if subject_exist:
                for i in range(1, 3):
                    sj_inf = request.env['subject.info'].sudo().search(
                        [('multiplier', '=', 3), ('subject', '=', subject_exist.id), ('semester', '=', i)], limit=1)
                    if not sj_inf:
                        request.env['subject.info'].sudo().create({
                            'subject': subject_exist.id,
                            'score': random.randint(1, 10),
                            'multiplier': 3,
                            'semester': i
                        })
                    for j in range(1, 6):
                        list1 = request.env['subject.info'].sudo().search(
                            [('multiplier', '=', 1), ('subject', '=', subject_exist.id), ('semester', '=', i)])
                        if len(list1) < 5:
                            sj_info1 = request.env['subject.info'].sudo().create({
                                'subject': subject_exist.id,
                                'score': random.randint(1, 10),
                                'multiplier': 1,
                                'semester': i

                            }),
                        list2 = request.env['subject.info'].sudo().search(
                            [('multiplier', '=', 2), ('subject', '=', subject_exist.id), ('semester', '=', i)])
                        if len(list2) < 5:
                            sj_info2 = request.env['subject.info'].sudo().create({
                                'subject': subject_exist.id,
                                'score': random.randint(1, 10),
                                'multiplier': 2,
                                'semester': i
                            })
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

    @http.route('/thpt/save/schedule', type='json', auth='user')
    def change_schedule(self, **kw):
        schedules = json.loads(request.httprequest.data)['schedules']
        for schedule in schedules:
            schedule_exist = request.env['schedule'].sudo().search([('id', '=', schedule['id'])])
            schedule_exist.write({
                'student_class': request.env['student.class'].sudo().search([('name', '=', schedule['_class']['name'])],
                                                                            limit=1).id,
                'date_of_week': schedule['date_of_week'] - 1,
                'subject': schedule['subject'],
                'semester': schedule['semester'],
                'teacher': request.env['teacher'].sudo().search([('id', '=', schedule['teacher']['id'])],
                                                                limit=1).id if schedule['teacher'] else None,
                'classroom': schedule['classroom'],
                'class_time': schedule['class_time'],
            })

        return schedules

    @http.route('/thpt/save/subject', type='json', auth='user')
    def change_subject(self, **kw):
        subjects = json.loads(request.httprequest.data)['subjects']
        for subject in subjects:
            subject_exist = request.env['subject'].sudo().search([('id', '=', subject['id'])])
            subject_exist.write({
                'teacher': subject['teacher']['id']
            })
            for subject_info in subject['subject_infos']:
                subject_info_exist = request.env['subject.info'].sudo().search([('id', '=', subject_info['id'])])
                subject_info_exist.write({
                    'score': subject_info['score'],
                    'multiplier': subject_info['multiplier'],
                })
        return subjects

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
                                                                        limit=1).id if res['main_teacher'] else None,
            'office_subject': request.env['office.subject'].sudo().search([('name', '=', res['subject'])],
                                                                          limit=1).id
        })

        return res

    @http.route('/thpt/add/class', type='json', auth='user')
    def add_class(self, **kw):

        res = json.loads(request.httprequest.data)
        _class = request.env['student.class'].sudo().create({
            'name': res['name'],
            'teacher': request.env['teacher'].sudo().search([('id', '=', res['teacher']['id'])],
                                                            limit=1).id,
        })
        for k in range(1, 3):
            for i in range(1, 6):
                for j in range(1, 7):
                    schedule = request.env['schedule'].sudo().create({
                        'student_class': _class.id,
                        'class_time': i,
                        'date_of_week': j,
                        'semester': k
                    })
        res['id'] = _class.id
        return res

    @http.route('/thpt/save/class', type='json', auth='user')
    def change_class(self, **kw):
        res = json.loads(request.httprequest.data)
        _class = request.env['student.class'].sudo().search([('id', '=', res['id'])])
        _class.write({
            'name': res['name'],
            'teacher': request.env['teacher'].sudo().search([('id', '=', res['teacher']['id'])],
                                                            limit=1).id,
        })
        for k in range(1, 3):
            for i in range(1, 6):
                for j in range(1, 7):
                    schedule = request.env['schedule'].sudo().search(
                        [('student_class', '=', _class.id), ('semester', '=', k), ('class_time', '=', i),
                         ('date_of_week', '=', j)])
                    if not schedule:
                        schedule = request.env['schedule'].sudo().create({
                            'student_class': _class.id,
                            'class_time': i,
                            'date_of_week': j,
                            'semester': k
                        })
        return res

    @http.route('/thpt/save/activity', type='json', auth='user')
    def change_activity(self, **kw):
        res = json.loads(request.httprequest.data)
        if res['id']:
            activity = request.env['extracurricular.activities'].sudo().search([('id', '=', res['id'])])
            print(activity.title)
            activity.write({
                'content': res['content'],
                'description': res['description'],
                'location': res['location'],
                'max_participants': res['max_participant'],
                'time': res['time'],
                'support_teacher1': res['support_teacher1']['id'],
                'support_teacher2': res['support_teacher2']['id'],
                'support_teacher3': res['support_teacher3']['id'],
                'teacher_in_charge': res['teacher_in_charge']['id'],
                'start_time': datetime.strptime(res['start_time'], '%Y-%m-%d'),
                'end_time': datetime.strptime(res['end_time'], '%Y-%m-%d'),
            })
        else:
            activity = request.env['extracurricular.activities'].sudo().create({
                'title': res['title'],
                'content': res['content'],
                'description': res['description'],
                'location': res['location'],
                'max_participants': res['max_participant'],
                'time': res['time'],
                'support_teacher1': res['support_teacher1']['id'],
                'support_teacher2': res['support_teacher2']['id'],
                'support_teacher3': res['support_teacher3']['id'],
                'teacher_in_charge': res['teacher_in_charge']['id'],
                'start_time': datetime.strptime(res['start_time'], '%Y-%m-%d'),
                'end_time': datetime.strptime(res['end_time'], '%Y-%m-%d'),
            })
            res['id'] = activity.id

        return res

    @http.route('/thpt/register/activity', type='json', auth='user')
    def register_activity(self, **kw):
        res = json.loads(request.httprequest.data)
        activity = request.env['extracurricular.activities'].sudo().search([('id', '=', res['activity_id'])], limit=1)
        user = request.env.user
        if user.role == 'student':
            student = request.env['student'].sudo().search([('user', '=', user.id)])
            student.extracurricular_activitie = activity.id
        print(res)

    @http.route('/thpt/save/outcome', type='json', auth='user')
    def change_outcome(self, **kw):
        outcomes = json.loads(request.httprequest.data)['outcomes']
        print(outcomes)
        for student in outcomes:
            for outcome in student['list_outcome']:
                outcome_exist = request.env['semester.outcome'].sudo().search(
                    [('id', '=', outcome['id']), ('semester', '=', outcome['semester'])], limit=1)
                outcome_exist.write({
                    'conduct': outcome['conduct'],
                    'academic_ability': outcome['academic_ability']
                })
        return outcomes
