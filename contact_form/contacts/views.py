from django.views import generic
from django.urls import reverse_lazy
from .forms import CorporateContactForm
from .models import CorporateContact
from django.template.loader import get_template
from accounts.models import CustomUser
from django.shortcuts import render, redirect


class CorporateContactCreate(generic.CreateView):
    model = CorporateContact
    form_class = CorporateContactForm
    template_name = 'contacts/corporate_contact_create.html'
    success_url = reverse_lazy('contacts:corporate_create')

    def form_valid(self, form):
        # 入力内容に問題がなければ呼ばれるメソッド

        # フォームの役割
        # 1. 入力欄を作る
        # 2. 送信されてきた入力内容を受け取る(値の検証や、型をPython用に変換してくれる)

        # テンプレートファイルに、辞書を渡して、メール本文の文字列を作成している
        subject = '題名'
        mail_text_template = get_template('contacts/email/corporate_message.txt')
        context = {
            'form': form,
        }
        # mail_textには、メールの本文が文字列で作られた状態
        mail_text = mail_text_template.render(context)

        # メールの送信処理
        for user in CustomUser.objects.all():  # モデル名.objects.all()
            print(user,user.is_received_email)
            if user.is_received_email:
                print(mail_text)
                # 実際にメールを送る。Userモデルに定義されている、メール送信用のメソッド
                user.email_user(subject, mail_text, 'info@a.com')

        # generic.CreateViewのform_validメソッドよぶ
        # form.save(保存処理のこと)と、リダイレクト処理をしている
        return super().form_valid(form)

# 確認画面を作る時
# 1. FormViewで、入力欄のあるページを作る CorporateContactInput
# 2. FormViewで、入力内容を表示する確認ページを作る CorporateContactConfirm
# 3. CreateViewで、入力内容を保存するビューを作る CorporateContactCreate

class CorporateContactInput(generic.FormView):
    """確認画面機能の、最初の入力ページ"""
    form_class = CorporateContactForm
    template_name = 'contacts/corporate_contact_input.html'

    def form_valid(self, form):
        # 入力内容に問題なければ呼ばれる
        context = {
            'form': form,
        }
        return render(
            self.request,
            'contacts/corporate_contact_confirm.html',
            context
        )

# CreateViewから、データの保存処理をなくしたビューがFormView
class CorporateContactInput(generic.FormView):
    """確認画面機能の、最初の入力ページ"""
    form_class = CorporateContactForm
    template_name = 'contacts/corporate_contact_input.html'

    def form_valid(self, form):
        context = {
            'form': form,
        }
        return render(
            self.request,
            'contacts/corporate_contact_input.html',
            context
        )


class CorporateContactConfirm(generic.FormView):
    form_class = CorporateContactForm

    def form_valid(self, form):
        context = {
            'form': form
        }
        return render(
            self.request,
            'contacts/corporate_contact_confirm.html',
            context
        )

    def form_invalid(self, form):
        context = {
            'form': form
        }
        return render(
            self.request,
            'contacts/corporate_contact_confirm.html',
            context
        )


class CorporateContactCreate(generic.CreateView):
    model = CorporateContact
    form_class = CorporateContactForm
    success_url = reverse_lazy('contacts:form_send_complete')

    def form_invalid(self, form):
        context = {
            'form': form
        }
        return render(
            self.request,
            'contacts/corporate_contact_input.html',
            context
        )

    def form_valid(self, form):
        # 入力内容に問題がなければ呼ばれるメソッド

        # モデルフォームのsaveメソッドで、DBに保存される
        # saveメソッドは、モデルインスタンスを返す
        corporate = form.save()

        # テンプレートファイルに、辞書を渡して、メール本文の文字列を作成している
        subject = '題名'
        mail_text_template = get_template('contacts/email/corporate_message.txt')
        context = {
            'corporate': corporate,
        }
        # mail_textには、メールの本文が文字列で作られた状態
        mail_text = mail_text_template.render(context)

        # メールの送信処理
        # モデル名.objects.filter(フィールド名=値)で、絞り込むことができます
        for user in CustomUser.objects.filter(is_received_email=True):
            # 実際にメールを送る。Userモデルに定義されている、メール送信用のメソッド
            user.email_user(subject, mail_text, 'info@a.com')

        return redirect('contacts:form_send_complete')


class FormSendComplete(generic.TemplateView):
    template_name = 'contacts/form_send_complete.html'