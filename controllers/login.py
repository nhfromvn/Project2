from odoo.addons.web.controllers.main import Home
from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import db_monodb, ensure_db, set_cookie_and_redirect, login_and_redirect
from odoo.tools.translate import _
import odoo

SIGN_UP_REQUEST_PARAMS = {'db', 'login', 'debug', 'token', 'message', 'error', 'scope', 'mode',
                          'redirect', 'redirect_hostname', 'email', 'name', 'partner_id',
                          'password', 'confirm_password', 'city', 'country_id', 'lang'}


class HomeInherit(Home):
    @http.route('/web/login', type='http', auth="none")
    def web_login(self, redirect='/thpt', **kwargs):
        ensure_db()
        request.params['login_success'] = False
        if request.httprequest.method == 'GET' and redirect and request.session.uid:
            return request.redirect(redirect)

        if not request.uid:
            request.uid = odoo.SUPERUSER_ID

        values = {k: v for k, v in request.params.items() if k in SIGN_UP_REQUEST_PARAMS}
        try:
            values['databases'] = http.db_list()
        except odoo.exceptions.AccessDenied:
            values['databases'] = None

        if request.httprequest.method == 'POST':
            old_uid = request.uid
            try:
                uid = request.session.authenticate(request.session.db, request.params['login'],
                                                   request.params['password'])
                user = request.env['res.users'].sudo().search([('id', '=', uid)])
                print(user)
                if user.role == request.params['role']:
                    request.params['login_success'] = True
                    return request.redirect(self._login_redirect(uid, redirect=redirect))
                else:
                    request.params['login_success'] = False
                    return request.render('thpt.error')
            except odoo.exceptions.AccessDenied as e:
                request.uid = old_uid
                if e.args == odoo.exceptions.AccessDenied().args:
                    values['error'] = _("Wrong login/password")
                else:
                    values['error'] = e.args[0]
        else:
            if 'error' in request.params and request.params.get('error') == 'access':
                values['error'] = _('Only employees can access this database. Please contact the administrator.')

        if 'login' not in values and request.session.get('auth_login'):
            values['login'] = request.session.get('auth_login')

        if not odoo.tools.config['list_db']:
            values['disable_database_manager'] = True
        response = request.render('web.login', values)
        response.headers['X-Frame-Options'] = 'DENY'
        return response
