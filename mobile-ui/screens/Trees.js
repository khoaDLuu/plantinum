import React from 'react';
import { StyleSheet, FlatList } from 'react-native';
import TreeListItem from '../components/TreeListItem';

export default class Trees extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      trees: [{
        "id": 1,
        "name": "Cactus",
        "url": "https://lh3.googleusercontent.com/9wXYl3-ZF4gXUBCgfQALGecQHgxWjZ4wi9L7VLtdGHgxpLOAP8eS49BhlwkyOYC8BE_ccbYd_BBYA0uuR-mIBUsvueywTOk8W6X_INaquC5sz2ESzslbw2wSVIwVK1_c2d5BXGGFH4TZsH5VNYEe-LevxRIOde6ykWOf89xK117_g_4PGCkcxfbsGvS1z_Qjje_JNBUgnt2RQpAXBWKlq30WxoBSo1I_-O3rE5hAwvxFYql5B__5uY3hdVtjj4kX3aW8APxnYtWx372oxYxV4VeuJjmpPgUAEYdHHzpKcfdUMLRsGmZ_l9s5O9z2tv3sNuBOsNB6N1_cYLdJX_F37ts1Ubt7ESdYaJvl-aFdtZqsqwb-DskaqyPlkPnrYH4oA2N7EIWQp4bMlKQGTbpzvxYvYQebzEAPhf_LAqpMQClxRIcblTKXGG91gR4VIzZMXY6Bas-rQ7cbBeQHJccVVhMJ7UyBOxGoueNjTrKoQ64ASQkoc4MtEMiuMJ_Dv-7VFDnovlN1JNGuUtqyIMuzl2hvlB5_NPxiSIoJQb1pfMHbDB5NOohmaRUzxuYmfz-84DDxlMRT4_IRRPF5Cgub3H7IAGGnVdL2mYnsAytI5qHj1ysbuW7G00-ytu2q7nyt2BSdDdkhohC5ro2uIIBfJZAhXLQjKO-hfo8TGEo8r2ogpCUlR_gcyg=s512-no",
        "temperature": "10%",
        "humidity": "50%",
        "moisture": "27%",
        "lightIntensity": "70%"
      },
      {
        "id": 2,
        "name": "Rose",
        "url": "https://lh3.googleusercontent.com/9aOMM843q1YpKBwxjlkYg1rwl9klHjZ8HJQhto0kVB5mok_IDlLFyXWH0sttOnUhmEucj2ZkN59LP66CUSyJwELoqCx3G4Q7ANie-bsJpUYQrOmTybf6Mk_kaXlW7Q4YcG43cypkuAdUhGVdNZfek5EAXjeok6Jtb8b88NPO8G1urIHC6goljbcPz1sYDCguV85VHMfhMu_AqDYEKBDjBdiRuOgGoo0buONwAD2J1zmeod9Vk91Na6WOJSwHjP_FXGEkw-q0UhF5ygGuU-d2pC1NOZOintoWtx0ABEwLRfD0El30--tF7y_4PW2wQZxJKFWQnFlPrIq-tPJngBiMrF0ZDkx_JIZHcyeReWrUFKLBBrtq0XmV3wPGQWfD8U9H5D1zo9Sz_YMZeWvXR2cc-McOMvaL9KYy_tEwJoNkoMlCDpcFBcW9AzgFRzi_BH7DRyVmmnhUTSniQLGllRGhHopCaS_Iz0lf9e2Pc-4N2gszvw7kMj20gB4_ilKdQ9Va64BZh8SOltKJZQMF3Gp4VvJU40sxc2xvWl6c-0tcybgY2FXBl3jcOlADEpEguZLljYRABwUA3oTCV0fJXNsJv7LUNW8w1347cWoh4QZJ6Rif1BIWGOV5hYNDF8Q6_7u1Tqo_N2La0U0dpS4cSOJxVSclsCetE7bmdjBpqpSvTgPLRHZ0ZCYACg=s512-no",
        "temperature": "20%",
        "humidity": "50%",
        "moisture": "27%",
        "lightIntensity": "70%"
      },
      {
        "id": 3,
        "name": "Orchid",
        "url": "https://lh3.googleusercontent.com/0isEaswrL6_Vavu-DsQssh_d3PNQlfxwO-A3SQbpxtj1cMrxDZNdjiAKzadfg0f6e9A2tcowJJYOhlpsRD1EmJC_luiVJ2aoY-tsxqfFc5Dg5LK4iZMmtjq4DpyL3vVGK-JW8SDAhsdyK9e1lTKBx2WZerRIxJaiCi71IYEijBJWXML5iCMhxiDQO9_KcdTgEXcvHVYVtB09q506K_0bnSoIctVRyiu_hEnrnQE2F9SZ-wTET78FR4u8wIG--LJuqDmGqO0yoZBzgj1zLMhvB15fTxzsINAWerO0CJTdBKPaiyzJmltHbUyNOz8oGB71_f0HhnPAWEFMT-CqbZQ2j-8dsZ-i4ax7VyiF8s2OPjBY2NKeFYgPQ3nmFhJIcDa9lbBayoVl5qiZJWcohspgXOBYzNBvzNER5Ao4nea8KxJtGLYVO8bAIdo86pzOTo0Txe03LmE61XzBtJE21DjJs493zCopdmJMffu94hoYVVNKh_DB_80P54buDP21ObpQUAyj9oQv2O2U5qDDEBMJUJBWXE7FaemOppAKvFw55JBqrnAiY8brISIzhIL5onnjwpf2oF5xyWsdO8HD2kulWbWKacJ9XWDcLI2f-loESyhmqZvY5fx_TpAEjadTm7mKxbTQeuEtSC6Yw_IUgmYj4RWUNXIqp_aKoWTkvS1QIUUIWjg26rokBg=s512-no",
        "temperature": "90%",
        "humidity": "50%",
        "moisture": "27%",
        "lightIntensity": "70%"
      },
      {
        "id": 4,
        "name": "Vera",
        "url": "https://lh3.googleusercontent.com/cUCbAJUAPxzZtIerPp368BiHGb4UllQM0Z0rqVmPj-3tqFV204pr8h5aBVidDlqj97Tsv59HQrDyV6R0e0wykTrh838C9t1LIZ9xVB2TM7dboZbQX66Gbpw9azd_fBSqhjnVOLoAQFDn9Py2kWeXOcrhbIKNiI3Iw5LuxBHuiS9NGS0vkDG5Lw8-Liay-4cJlaSSOvn6l98NNWGHZ9wSJIOUqQOq95Tcf5ph9Pg0MQdoWkdZuVN6StYiFrkLq11uOYEmpt78wJMfA-Pp4yXlZP38QjmTXDpqi0TZfMpqsuhTIOIwvp7SELaf_LO_wu6YdPC2J_y2IBl3bxd7YkTH8yLmQikhdhWZuD5dtgAI4JwIeECp-VWGVd8Z6lus5wDofQHysz3KKDWSs2lkZM510IrZHrKboD33hVAkO89mvxs_27GGX6G3digkPx5U6mu9bM3ftibKCMxPW62wu6uIBnEqkhdw-9q9urwaAwAU22zjqKz9eTajWpoW5_5Oewa41TT4flSbEvFAQ23uv3bu3UcsMOKXU-ffhbVdpdylRnBupzRGdepoMnFVSeO5AfIqhvzm8W2XHEfyy8n9-2VeRv71X7IEJboOgsWKP-A07tnz1s_kHUO7BCLEiWFO3O3dr_FNPyJb6G7Tht-H6IvZcXpu0x76sRQC_Bd1cc12U_GKyt7cRk2-RA=s512-no",
        "temperature": "20%",
        "humidity": "50%",
        "moisture": "27%",
        "lightIntensity": "70%"
      },
      {
        "id": 5,
        "name": "papaya flower",
        "url": "https://lh3.googleusercontent.com/Hr6KJz7-W6RXDtNrWbSwtGnQ5UA5_pxqR-fp8CaQ5oTPZxGlXyTdr50G0iQH7IELoIz74IIK__U2F8YMgEjZFAPlztgXit8t_wKoyvvgkkBZBvwh4iS__p5m9FZGyOX0w-bWJArhGzfdguhibSVv_rkI5mutHwNBlKVzo6FFvTp3hEu9kR5HWrtJSvrdI6QEHGPkIoOFZY0f86iGmepaJaHBB2400vujDDaGd4rWxEXl0GPXtmlh73F7X-5YaacNJ7C7tbFh20GL1Iad6CG0tnuS2cpoOZIcbeL7wcQqmYh4DQpO74XoVouWWPl4Wjdwwv6cCmhtM1vcXvGSwS8Cpzdjmi_bLhKP8fh4myH5_fZbElymVOm0I8FqJBxG0KQt5i-FHKCpVM68KzydA3Fno5lHNmtDdoqP9u84YuW-gHDZ1WVgo6RpnU3E0FoQ_DTypn1XMDvOivy_EanN4FwDv5mjcnsg7_4cWUMpI7f7i6d5JxOjqrszWGRcSqvx2HADAb9UuMQedcns-8hrY1bIo00FuUQq_PZpa98UWYlQgWxmk0lfSf0aJDuDd-6Hj3Ks3nZrE0NefY1S0YdEcI7Ga6e_1mGLplxljkdJI-uRy7zhaZU-KfEUmay0jl95KD7dTlby5lCC8LP5iheHyxI1pafHlxzUane8tF2J0ew4LL_UE34QJzB4Rw=s512-no",
        "temperature": "50%",
        "humidity": "50%",
        "moisture": "27%",
        "lightIntensity": "70%"
      },
      {
        "id": 6,
        "name": "Honeysuckle",
        "url": "https://lh3.googleusercontent.com/RwNe5QDCkc2btbCzUVvKB_1LFI0Bc-BRUFz7Sk7ZEe9ymPK7zsfaW4zdEVoShGNrqN2DtuZ6vrbfLocpjL4O6aPkUaX7XgVOX258LOy025sg0T69TY8a3VwSizEQtN6GAwMMNVLNr3hG5CZHCS7k5ovYoDccOHiTBiPp3oW3JaDfvujotUKfQPG1jQ7U7lLhJ_P5WD6eUld4oqgjLu8k3-9W_RUcleb_ewt0nX6z9__X0rs8mEU8C501rfaXut4MW8vXgeTvfs1rRujo4qrjg4oknvtOfypS9Ql3HuUceLzRpRMfJhS34WR9yPnRoA42CVHfL3rulxzCG7CDK4FwciVq1yrvBTLCfufazYezYEAFOIaBOu-Y66k4yVNHUTra5yEFyH653FgXLGYnsUOonKPsFK2vhWUTBRAbhyoez0ih91oKEp9RydfAF3Gv_DN7T695CSKdJ6XBrYr2jl4kuII5muJyR3gD0LAfwf1hBEFai0elWGRg6H-LOtAfAOO7uZZibSc1L-BfkGD9xrNq8uMI4uoRh3MpOSpefqfixxLX7iJzeEqM7Jt_g_VrwXq7QyfLGX1gHT4vMGmwuEAdB_TyDbSQW1n3eCNCPdiZwqBSNIr8wWy6brYVrXIFWVlpQzqdb_91umY5bSLsIGjO3g91qkilYKCjNGwi0Ivw1kT2eaqCJXqpKA=s512-no",
        "temperature": "40%",
        "humidity": "50%",
        "moisture": "27%",
        "lightIntensity": "70%"
      },
    ]
    };
  }
  render() {
    const { navigation } = this.props;
    const { trees } = this.state;
    return (
        <FlatList 
          data={trees}
          renderItem={({ item }) => 
          <TreeListItem tree={item}
            onPress={() => navigation.navigate('Home2', {
              treeName: item.name,
              imageUrl: item.url,
              temperature: item.temperature,
              humidity: item.humidity,
              moisture: item.moisture,
              lightIntensity: item.lightIntensity
            })}
          />}
          keyExtractor={item => `${item.id}`}
          contentContainerStyle={styles.container}
        />
    );
  }
}

const styles = StyleSheet.create({
  container: {
    paddingTop: 16,
    paddingHorizontal: 16,
    backgroundColor: "#58B0AE",
  },
});
