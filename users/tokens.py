from django.contrib.auth.tokens import PasswordResetTokenGenerator


#generazione dei token da inviare per la verifica della mail
class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            str(user.is_active) + str(user.pk) + str(timestamp)
        )

token_generator = AccountActivationTokenGenerator()