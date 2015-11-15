#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Al-Rama Lahan <lahangit@gmail.com>.
"""Run project, choosing which configuration to apply."""

import os
import sys
import argparse


def get_arguments(argv):
    """Get arguments from command line."""
    parser = argparse.ArgumentParser(description='Run a Flask application')
    parser.add_argument('-c', '--config',
                        default='dev',
                        help='Which configuration to use:`dev`, `pro` `test`. \
                        It defaults to `dev`')
    parser.add_argument('-r', '--run',
                        default='python manage.py runserver',
                        action='store_true',
                        help='Which command manage.py will run.')
    parser.add_argument('-o', '--options',
                        default='debug true, reload true',
                        action='append',
                        help='Additional options to run')
    parser.add_argument('-hh', '--host',
                        default='localhost',
                        action='store_true',
                        help='Host to use for running the application.\
                        Defaults to `localhost`.')
    parser.add_argument('-p', '--port',
                        default=5000,
                        action='store_true',
                        help='Port to use for running the application.\
                        Defaults to port 5000.')
    args = parser.parse_args()
    return args


def main(args):
    """Process received arguments."""
    options = args.options

    if args.config == 'pro':
        os.environ['APP_CONFIG'] = "project.config.ProductionConfig"
        env = "Production configuration"
    elif args.config == 'test':
        os.environ['APP_CONFIG'] = "project.config.TestingConfig"
        env = "Testing configuration"
    else:
        os.environ['APP_CONFIG'] = "project.config.DevelopmentConfig"
        env = "Development configuration"

    options = list(args.options.split(' '))
    return args, env, options


if __name__ == "__main__":
    """Application entry point."""
    args = get_arguments(sys.argv)
    args, env, options = main(args)

    from werkzeug.serving import run_simple
    from project import app

    print(" * Serving {app} at \
          http://{host}:{port}/\n * Config: {env}".format(app=app,
                                                          host=args.host,
                                                          port=args.port,
                                                          env=env))
    run_simple(args.host, args.port, app,
               use_reloader=True,
               use_debugger=True,
               reloader_type='watchdog')
