package a4.folio.Model.DataReceiver;

import a4.folio.Model.DataClasses.BourseInformation;
import retrofit2.Call;
import retrofit2.http.GET;

/**
 * Created by amir on 4/18/2018.
 */

interface FolioClient {
    @GET("/api/getBourseInfo")
    Call<BourseInformation> getBourseInformation();
}
