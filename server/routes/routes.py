from flask import render_template


def define_routes(app):
    @app.route('/', methods=['GET'])
    def index():
        return render_template('index.html')

    # Serve Static Assets
    # TODO: Do this with apache or nginx
    @app.route('/static/<path:file_path>.<extension>', methods=['GET'])
    def static_proxy(file_path, extension):
        file_path = file_path.rstrip('/') + "." + extension
        app.logger.info('File Path: %s' % file_path)
        return app.send_static_file(file_path)
