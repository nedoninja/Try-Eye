using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Try_Eye
{
    public partial class Form1 : Form
    {

        public Form1()
        {
            InitializeComponent();
            String res = run_cmd("\"services\\venv\\Scripts\\python.exe\"", "\"services\\Check.py\"");
            string[] tempList = res.Split(new char[] { ' ' });
            foreach (var item in tempList)
            {
                if (item.Contains("False"))
                {
                    MessageBox.Show("ошибка обрудования, попробуйте ещё раз");
                    Application.Exit();
                    this.Close();
                    Console.WriteLine("ds");
                }
            }

            label3.Text = "OK";
            label4.Text = "OK";
            label5.Text = "OK";

        }

        private void button1_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private String run_cmd(string cmd, string args)
        {
            ProcessStartInfo start = new ProcessStartInfo();
            start.WindowStyle = ProcessWindowStyle.Hidden;
            start.FileName = cmd;
            start.Arguments = args;
            start.UseShellExecute = false;
            start.RedirectStandardOutput = true;
            using (Process process = Process.Start(start))
            {
                using (StreamReader reader = process.StandardOutput)
                {
                    string result = reader.ReadToEnd();
                    return result;
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            var fm = new Form2();
            fm.Show();
            Hide();
        }
    }
}
