package com.KP.News;

import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.core.view.GravityCompat;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.KP.News.Api.RetrofitClient;
import com.KP.News.adapter.NewsSummery;
import com.KP.News.model.NewsBO;
import com.google.android.material.navigation.NavigationView;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class MainActivity extends AppCompatActivity implements NavigationView.OnNavigationItemSelectedListener {

RecyclerView allbidsrecyclerview;
Button sports,news;
TextView type;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        allbidsrecyclerview = (RecyclerView) findViewById(R.id.allbidsrecyclerview);
        ImageView menuRight = (ImageView) findViewById(R.id.menuRight);

        // news = (Button) findViewById(R.id.news);
        //sports = (Button) findViewById(R.id.sports);
        type = (TextView) findViewById(R.id.type);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
//        try {
//            this.getSupportActionBar().hide();
//        }
//        catch (Exception ex)
//        {
//            ex.getMessage();
//        }
        //toolbar.setTitle("Assessment");
        setSupportActionBar(toolbar);
        getnews("News");
//        news.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View view) {
//                getnews("News");
//                type.setText("News");
//                news.setBackground(getResources().getDrawable(R.color.teal_200));
//                sports.setBackground(getResources().getDrawable(R.color.purple_500));
//
//            }
//        });
//        sports.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View view) {
//                getnews("Sports");
//                type.setText("Sports");
//                news.setBackground(getResources().getDrawable(R.color.purple_500));
//                sports.setBackground(getResources().getDrawable(R.color.teal_200));
//
//            }
//        });
        final DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_home);
        menuRight.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (drawer.isDrawerOpen(GravityCompat.END)) {
                    drawer.closeDrawer(GravityCompat.END);
                }
                else {
                    drawer.openDrawer(GravityCompat.END);
                }
            }
        });
        NavigationView navigationView2 = (NavigationView) findViewById(R.id.nav_view2);
        navigationView2.setNavigationItemSelectedListener(this);


    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }


    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
//        if (id == R.id.action_settings) {
//            return true;
//        }

        return super.onOptionsItemSelected(item);
    }

    @SuppressWarnings("StatementWithEmptyBody")
    @Override
    public boolean onNavigationItemSelected(MenuItem item) {
        // Handle navigation view item clicks here.
        int id = item.getItemId();
        String text = "";

        if (id == R.id.nav_home) {
            getnews("Sports");
            type.setVisibility(View.VISIBLE);
                type.setText("Sports");

               // news.setBackground(getResources().getDrawable(R.color.Truewhite));
               // sports.setBackground(getResources().getDrawable(R.color.online));
        }

        else if (id == R.id.nav_news) {
            getnews("News");
            type.setVisibility(View.GONE);
               // news.setBackground(getResources().getDrawable(R.color.Truewhite));
                //sports.setBackground(getResources().getDrawable(R.color.online));
        }
        else if (id == R.id.nav_politics) {
            getnews("Politics");
                type.setText("Politics");
            type.setVisibility(View.VISIBLE);

            // news.setBackground(getResources().getDrawable(R.color.Truewhite));
                //sports.setBackground(getResources().getDrawable(R.color.online));
        }
        else if (id == R.id.nav_tech) {
            getnews("Technology");
                type.setText("Technology");
            type.setVisibility(View.VISIBLE);


        }
        else if (id ==R.id.nav_ente){
            getnews("Entertainment");
                type.setText("Entertainment");
            type.setVisibility(View.VISIBLE);


        }


        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_home);
        drawer.closeDrawer(GravityCompat.END);
        return true;
    }
    private void getnews(String type) {
        Call<NewsBO> call;
        if(type.equalsIgnoreCase("News")) {
            call = RetrofitClient.getInstance().getMyApi().getsuperHeroes();
        }
        else if(type.equalsIgnoreCase("Politics"))
        {
            call = RetrofitClient.getInstance().getMyApi().getsuperpolitics();
        }
        else if(type.equalsIgnoreCase("Technology"))
        {
            call = RetrofitClient.getInstance().getMyApi().getsupertechnlogy();
        }
        else if(type.equalsIgnoreCase("Entertainment"))
        {
            call= RetrofitClient.getInstance().getMyApi().getsuperentertainment();
        }
        else
        {
            call = RetrofitClient.getInstance().getMyApi().getsuperSports();
        }
        call.enqueue(new Callback<NewsBO>() {
            @Override
            public void onResponse(Call<NewsBO> call, Response<NewsBO> response) {
                NewsBO myheroList = response.body();
//                ArrayList<ArticlesBO> assestBOList = new ArrayList<ArticlesBO>();
//                Gson gson=new GsonBuilder().setFieldNamingPolicy(FieldNamingPolicy.IDENTITY).create();
//                assestBOList.addAll(Arrays.asList(gson.fromJson(response.toString(),ArticlesBO[].class)));
                LinearLayoutManager layoutManager = new LinearLayoutManager(MainActivity.this);
                allbidsrecyclerview.setLayoutManager(layoutManager);
                NewsSummery newsSummery =new NewsSummery(myheroList.getArticles(),MainActivity.this);
                allbidsrecyclerview.setAdapter(newsSummery);
                newsSummery.notifyDataSetChanged();
                allbidsrecyclerview.setVisibility(View.VISIBLE);
            }

            @Override
            public void onFailure(Call<NewsBO> call, Throwable t) {
                Toast.makeText(getApplicationContext(), "An error has occured", Toast.LENGTH_LONG).show();
            }

        });
    }



    @Override
    public void onPointerCaptureChanged(boolean hasCapture) {
        super.onPointerCaptureChanged(hasCapture);
    }
}