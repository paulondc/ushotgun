import os
import shotgun_api3

class Session(object):
    """
    Singleton shotgun session.
    """
    __session = None

    @classmethod
    def get(cls):
        """
        Return the current session.
        """
        if cls.__session is None:

            # taking care of the authentication, so we don't need to do that in the task.
            # this is going to be available as a global object
            cls.__session = shotgun_api3.Shotgun(
                os.environ['UMEDIA_SHOTGUN_URL'],
                script_name="Toolkit",
                api_key="7839b54042ddfecdc6d0bd27e72c4499d5c04516f96dc1ff30d9bb7ac084ec7e"
            )

        return cls.__session
