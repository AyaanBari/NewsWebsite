package com.KP.News.adapter;

import android.annotation.SuppressLint;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.net.Uri;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.ProgressBar;
import android.widget.TextView;
import android.widget.Toast;

import androidx.cardview.widget.CardView;
import androidx.recyclerview.widget.RecyclerView;

import com.KP.News.R;
import com.KP.News.model.ArticlesBO;
import com.squareup.picasso.Callback;
import com.squareup.picasso.Picasso;

import java.util.HashMap;
import java.util.List;


public class NewsSummery extends RecyclerView.Adapter< NewsSummery.DataObjectHolder> {
    List<ArticlesBO> mdataset;
    private final Context context;
    private int calculateqty=0;
    private double totalqty;
    private static int Count = 1;
    TextView remaining;

    int row_index =-1;

    View view;
    public HashMap<Integer, View> checkBoxes = new HashMap<Integer, View>();
    private int randomNum;

    public NewsSummery(List<ArticlesBO> mdataset, Context context) {
        this.mdataset = mdataset;
        this.context = context;
    }

    @Override
    public NewsSummery.DataObjectHolder onCreateViewHolder(ViewGroup parent, int viewType) {

        view= LayoutInflater.from(parent.getContext()).inflate(R.layout.imagelists,parent,false);
        NewsSummery.DataObjectHolder dataObjectHolder=new NewsSummery.DataObjectHolder(view);

        return dataObjectHolder;
    }

    @Override
    public void onBindViewHolder(final NewsSummery.DataObjectHolder holder, @SuppressLint("RecyclerView") final int position) {
        try {



            //Picasso.with(context).load(imageurl).into(imageView);
               // holder.img.setImageBitmap(decodedByte1);

                holder.description.setText(mdataset.get(position).getTitle());
                holder.adescription.setText(mdataset.get(position).getDescription());
                holder.date.setText(mdataset.get(position).getPublishedAt());


                if(mdataset.get(position).urlToImage !=null) {
                    holder.img.setVisibility(View.VISIBLE);
                    Picasso.with(context)
                            .load(mdataset.get(position).getUrlToImage())
                            .into(holder.img, new Callback() {
                                @Override
                                public void onSuccess() {
                                }

                                @Override
                                public void onError() {

                                }
                            });
                }
                else
                {
                    holder.img.setVisibility(View.GONE);
                }

                holder.ridehistorycardView.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View view) {

                        if(mdataset.get(position).getUrl()!=null) {
                            Intent browserIntent = new Intent(Intent.ACTION_VIEW, Uri.parse(mdataset.get(position).getUrl()));
                            context.startActivity(browserIntent);
                        }
                        else
                        {
                            Toast.makeText(context,"No External Link Found",Toast.LENGTH_SHORT).show();
                        }
                    }
                });


        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
    }

    private BroadcastReceiver mMessageReceiver = new BroadcastReceiver() {
        @Override
        public void onReceive(Context context, Intent intent) {
            // Get extra data included in the Intent
            int message = intent.getIntExtra("message",0);

            Log.d("receiver", "Got message: " + message);
            notifyItemChanged(message);
        }
    };

    @Override
    public int getItemCount() {
        return mdataset.size();
    }

    public class DataObjectHolder extends RecyclerView.ViewHolder {
        TextView description,adescription,date;
        ImageView img;
        ProgressBar progressBar;
        CardView ridehistorycardView;

        public DataObjectHolder(View itemView) {
            super(itemView);
            img =   (ImageView) itemView.findViewById(R.id.img);
            description =   (TextView)itemView.findViewById(R.id.description);
            adescription =   (TextView)itemView.findViewById(R.id.adescription);
            date =   (TextView)itemView.findViewById(R.id.date);
            ridehistorycardView =   (CardView)itemView.findViewById(R.id.ridehistorycardView);
            //progressBar =   (ProgressBar) itemView.findViewById(R.id.homeprogress);

        }
    }


}
