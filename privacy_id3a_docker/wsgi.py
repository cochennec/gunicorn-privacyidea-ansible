from privacyidea.app import create_app
app = create_app(config_name='production', silent=True)

if __name__ == "__main__":
    application.run()
