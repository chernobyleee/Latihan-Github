<?php

class Latihan1 extends CI_Controller
{
    public function index()
    {
        echo "Selamat Datang.. Selamaat Belajar WP";
    }

    public function penjumlahan($n1,$n2)
    {
        $this->load->model('Model_latihan');
        $data['nilai1'] = $n1;
        $data['nilai2'] = $n2;
        $data['hasil'] = $this->Model_latihan->jumlah($n1, $n2);
        $this->load->view('view_latihan', $data);
        }
}
?>