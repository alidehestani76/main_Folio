package a4.folio;

import android.os.CountDownTimer;
import android.support.v4.app.FragmentManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.FrameLayout;

public class MainActivity extends AppCompatActivity {
    FrameLayout frameLayout ;
    FragmentManager fragmentManager ;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.logo_page);
        CountDownTimer countDownTimer = new CountDownTimer(1000, 1000) {
            @Override
            public void onTick(long millisUntilFinished) {

            }

            @Override
            public void onFinish() {
                setContentView(R.layout.main_page);
                frameLayout = (FrameLayout) findViewById(R.id.main_frameLayout);
                fragmentManager = getSupportFragmentManager();
                loginPage();
            }
        };
        countDownTimer.start();
    }

    private void loginPage(){

    }
}
