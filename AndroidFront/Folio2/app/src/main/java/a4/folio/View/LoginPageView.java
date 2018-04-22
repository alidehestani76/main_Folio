package a4.folio.View;

import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;

import a4.folio.Controller.SignIn;
import a4.folio.R;

/**
 * Created by amir on 4/21/2018.
 */

public class LoginPageView extends Fragment {
    EditText username, password;
    Button signInButton, createAccount;

    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.login_page, container, false);
        username = (EditText) view.findViewById(R.id.login_username_editText);
        password = (EditText) view.findViewById(R.id.login_password_editText);
        signInButton = (Button) view.findViewById(R.id.login_signIn_button);
        createAccount = (Button) view.findViewById(R.id.login_createAccount_button);
        signInButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                SignIn.signIn(username.getText().toString(), password.getText().toString());
            }
        });
        createAccount.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //go to create account
            }
        });


        return view;
    }


}
