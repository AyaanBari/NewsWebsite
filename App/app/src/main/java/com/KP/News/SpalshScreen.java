package com.KP.News;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;

public class SpalshScreen extends AppCompatActivity {
    private static long SLEEP_TIME = 3;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_spalsh_screen);
        new IntentLauncher().start();
    }
    private class IntentLauncher extends Thread {
        public void run() {
            try { sleep(SLEEP_TIME * 1000); } catch (Exception e) {;}

            try {
                    Intent intent = new Intent(SpalshScreen.this,MainActivity.class);
                    startActivity(intent);
                    finish();

            }
            catch (Exception ex)
            {

                ex.getMessage();
            }

        }
    }
}