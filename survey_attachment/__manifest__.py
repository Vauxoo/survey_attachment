# -*- encoding: utf-8 -*-

{
    'name': 'Survey Attachment',
    'version': '11.0',
    'website': "https://www.fogits.com/",
    'category': 'Survey',
    'description': """
        Add attachment to survey
    """,
    'depends': ["base","survey","website"],
    'data': [
        'views/survey_question_template.xml',
        'views/survey_user_input_line_view.xml',
    ],
}
