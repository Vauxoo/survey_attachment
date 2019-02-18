# -*- encoding: utf-8 -*-

{
    'name': 'Survey Attachment',
    'summary': """
    This module add new type of question on Survey Upload file """,
    'version': '11.0',
    'website': "https://www.fogits.com/",
    'category': 'Survey',
    'description': """
        Add attachment to survey
    """,
    'author': "Fogits Solutions",
    'images': ['static/description/survey.jpg'],
    'depends': ["base","survey","website"],
    'data': [
        'views/survey_question_template.xml',
        'views/survey_user_input_line_view.xml',
    ],
}
