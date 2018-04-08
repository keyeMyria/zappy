import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs/Observable';

import { environment } from '../../environments/environment';


@Component({
  selector: 'app-feed',
  templateUrl: './feed.component.html',
  styleUrls: ['./feed.component.css']
})
export class FeedComponent implements OnInit {
  
  feed: any;
  full_feed: any;
  
  handle: string = "";

  username: string;
  count: number;
  
  message: string;
  error = false;

  baseUrl = environment.baseUrl;
  private endpoint = this.baseUrl + '/api/twitter/feed/';

  constructor(private http: HttpClient) { }

  ngOnInit() {
    console.log(this.baseUrl);
    this.getFeed();
  }
  
  goFetch(): void {
    if (this.username == null) {
      this.error = true;
      this.message = "username field is required.";
    } else {
      this.message = "going to fetch the world!!";

      this.http.post(
        this.baseUrl + '/api/twitter/feed/go_fetch/', 
        {'handle': this.username, 'count': this.count }
      ).subscribe(
      data => { this.message = null; },
        err => console.error(err)
      );
    }    
  }

  getFeed(): void {
    console.log(this.endpoint);
    this.http.get(this.endpoint).subscribe(
      data => { this.full_feed = data; this.feed = this.full_feed },
      err => console.error(err),
      () => console.log('done loding feed')
    );
  }
  
  withUsername(event: any): void {
    this.handle = event.target.value;
    if (this.handle != "") {
      this.feed = this.full_feed.filter(
        tweet => tweet.handle == this.handle
      );
    } else {
      this.feed = this.full_feed;
    }
  }
}
